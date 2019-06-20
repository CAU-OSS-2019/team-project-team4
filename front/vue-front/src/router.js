import Vue from "vue";
import Router from "vue-router";
import DashboardLayout from "@/layout/DashboardLayout";
import AuthLayout from "@/layout/AuthLayout";
import BrowserSource from "@/views/BrowserSource.vue";
Vue.use(Router);

export default new Router({
    mode: "history",
    linkExactActiveClass: "active",
    routes: [{
            path: "/",
            redirect: "default",
            component: AuthLayout,
            children: [{
                path: "/",
                name: "default",
                component: () =>
                    import ( /* webpackChunkName: "demo" */ "./views/Default.vue")
            }]
        },
        {
            path: "/",
            component: DashboardLayout,
            children: [{
                path: "/dashboard",
                name: "dashboard",
                // route level code-splitting
                // this generates a separate chunk (about.[hash].js) for this route
                // which is lazy-loaded when the route is visited.
                component: () =>
                    import ( /* webpackChunkName: "demo" */ "./views/Dashboard.vue")
            }]
        },
        {
            path: "/browsersource",
            name: "/browsersource",
            component: BrowserSource
        }
    ]
});