import datetime
from sqlalchemy import Column, Integer, Float
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql.sqltypes import DateTime

from database.mysql import Base, engine, get_db
from errors import UnicornException


class FlatItem(Base):
    __tablename__ = "flats"

    id = Column(Integer, primary_key=True)
    hot_water = Column(Float)
    cold_water = Column(Float)
    day_el = Column(Float)
    night_el = Column(Float)
    last_month_hot_water = Column(Float)
    last_month_cold_water = Column(Float)
    last_month_day_el = Column(Float)
    last_month_night_el = Column(Float)
    flat_number = Column(Integer)
    date_create = Column(DateTime, default=datetime.datetime.utcnow)
    date_update = Column(DateTime, onupdate=datetime.datetime.utcnow)

    @classmethod
    def get_flats(cls):
        query = text("SELECT * FROM flats")
        try:
            result = get_db().execute(query).all()
        except:
            raise UnicornException(name="Internal_err")

        return result

    @classmethod
    async def get_flat(cls, flat_id: int):
        query = text(f"SELECT * FROM {cls.__tablename__} WHERE id=%s" % flat_id)
        try:
            flat = get_db().execute(query).first()
        except SQLAlchemyError as e:
            print(e)
            raise UnicornException(name="db_not_connected")
        except Exception as e:
            raise UnicornException(name="Internal_err")
        return flat

    @classmethod
    async def update_flat(cls, flat_id: int, new_data):
        query = text(f"""
            UPDATE flats
            SET
                hot_water = {new_data.new_hot_water},
                cold_water = {new_data.new_cold_water},
                day_el = {new_data.new_day_el},
                night_el = {new_data.new_night_el},
                last_month_hot_water = {new_data.hot_water},
                last_month_cold_water = {new_data.cold_water},
                last_month_day_el = {new_data.day_el},
                last_month_night_el = {new_data.night_el}
            WHERE id = {flat_id}
            """)

        try:
            with get_db() as connection:
                connection.execute(query)
                connection.commit()
        except Exception as e:
            raise UnicornException(name="Internal_err")

        return {
            "status_code": 200,
            "message": "all ok",
        }

    @classmethod
    def delete_flat(cls):
        pass

    @classmethod
    async def get_result(cls, flat_id: int):
        flat = await cls.get_flat(flat_id)
        flat_dict = {key: flat[index] for index, key in enumerate(flat.keys())}
        hot_water = cls.get_hot_water(flat_dict.get("hot_water"), flat_dict.get("last_month_hot_water"), flat_dict.get("flat_number"))
        cold_water = cls.get_cold_water(flat_dict.get("cold_water"), flat_dict.get("last_month_cold_water"), flat_dict.get("flat_number"))
        day_el = cls.get_day_el(flat_dict.get("day_el"), flat_dict.get("last_month_day_el"), flat_dict.get("flat_number"))
        night_el = cls.get_night_el(flat_dict.get("night_el"), flat_dict.get("last_month_night_el"), flat_dict.get("flat_number"))
        water_drain = cls.get_water_drain(hot_water[2] + cold_water[2], flat_dict.get("flat_number"))
        water_heating = cls.get_water_heating(hot_water[2], flat_dict.get("flat_number"))
        total = sum([hot_water[1], cold_water[1], day_el[1], night_el[1], water_drain[1], water_heating[1]])
        text_result = f"""
??????????????????????????
{day_el[0]}
{night_el[0]}
????????
{cold_water[0]}
{hot_water[0]}
{water_drain[0]}
{water_heating[0]}
??????????: {round(total, 2)}
            """
        return {
            "status_code": 200,
            "result": text_result,
        }

    @staticmethod
    def get_hot_water(hot_water, last_month_hot_water, flat_number):
        hot_water_diff = hot_water - last_month_hot_water
        if flat_number == 256:
            price = 28.01
        else:
            # 81
            price = 25.26
        hot_water_price = round(hot_water_diff * price, 2)

        return [
            f"?????????????? ????????: {hot_water} - {last_month_hot_water}. {hot_water_diff} x {price} = {hot_water_price}",
            hot_water_price,
            hot_water_diff
        ]

    @staticmethod
    def get_cold_water(cold_water, last_month_cold_water, flat_number):
        cold_water_diff = cold_water - last_month_cold_water
        if flat_number == 256:
            price = 28.01
        else:
            # 81
            price = 25.26
        cold_water_price = round(cold_water_diff * price, 2)

        return [
            f"???????????????? ????????: {cold_water} - {last_month_cold_water}. {cold_water_diff} x {price} = {cold_water_price}",
            cold_water_price,
            cold_water_diff
        ]

    @staticmethod
    def get_day_el(day_el, last_month_day_el, flat_number):
        day_el_diff = day_el - last_month_day_el
        if flat_number == 256:
            price = 4.61
        else:
            # 81
            price = 4.33
        day_el_price = round(day_el_diff * price, 2)

        return (
            f"????????: {day_el} - {last_month_day_el}. {day_el_diff} x {price} = {day_el_price}",
            day_el_price
        )

    @staticmethod
    def get_night_el(night_el, last_month_night_el, flat_number):
        night_el_diff = night_el - last_month_night_el
        if flat_number == 256:
            price = 1.76
        else:
            # 81
            price = 1.6
        night_el_price = round(night_el_diff * price, 2)

        return f"????????: {night_el} - {last_month_night_el}. {night_el_diff} x {price} = {night_el_price}", night_el_price

    @staticmethod
    def get_water_drain(water_sum, flat_number):
        if flat_number == 256:
            price = 33.4
        else:
            # 81
            price = 30.38
        water_drain_price = round(water_sum * price, 2)

        return f"??????????????????????????: {water_sum} * {price} = {water_drain_price}", water_drain_price

    @staticmethod
    def get_water_heating(hot_water, flat_number):
        if flat_number == 256:
            price = 2367.38
        else:
            # 81
            price = 2196.4
        water_heating_price = round(price * 0.051 * hot_water, 2)

        return f"????????????????????: {price} * 0,051 * {hot_water} = {water_heating_price}", water_heating_price
