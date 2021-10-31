const getService = async (url_path) => {
    let url = '';
    if (process.env.VUE_APP_BACKEND_PORT) {
        url = `${window.location.protocol}//${window.location.hostname}${process.env.VUE_APP_BACKEND_PORT}${url_path}`;
    } else {
        url = `${window.location.protocol}//${window.location.hostname}${url_path}`;
    }
    return await fetch(url, {
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:9091',
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
        .then(data => data.json())
        .then(data => {
            return data;
        })
        .catch(err => console.log(err));
}

const postService = async (url_path, data) => {
    let url = '';
    if (process.env.VUE_APP_BACKEND_PORT) {
        url = `${window.location.protocol}//${window.location.hostname}${process.env.VUE_APP_BACKEND_PORT}${url_path}`;
    } else {
        url = `${window.location.protocol}//${window.location.hostname}${url_path}`;
    }
    return await fetch(url, {
        method: 'put',
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:9091',
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: JSON.stringify(data),
    })
        .then(data => data.json())
        .then(data => {
            return data;
        })
        .catch(err => console.log(err));
}

module.exports = {
    getService,
    postService
}