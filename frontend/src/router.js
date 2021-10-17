import Index from '/src/components/Index'
import { FlatItem, FlatsList, ResultItem } from '/src/components/flats/init'

export default {
    routes: [
        {
            path: '/',
            name: 'index',
            component: Index
        },
        {
            path: '/flats',
            name: 'flats',
            component: FlatsList
        },
        {
            path: '/flats/:id',
            name: 'flat-item',
            component: FlatItem
        },
        {
            path: '/flats/result/:id',
            name: 'result',
            component: ResultItem
        }
    ],
}