import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import BookInfo from '../components/books/BookInfo.vue'
import { el } from 'element-plus/es/locale'
import { useUserInfoStore } from '@/stores/userinfo.store'
import { RouterView } from 'vue-router'

const userinfoStore = useUserInfoStore()
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/home',
      redirect: '/home/admin-home',
      name: 'home',
      component: HomeView,
      // meta: {
      //   title: '图书推荐系统'
      // },
      children: [
        {
          path: 'admin-home',
          name: 'admin-home',
          component: () => import('@/components/home/AdminHome.vue'),
          meta: {
            title: '首页'
          }
        },
        {
          path: 'users',
          name: 'users',
          component: RouterView,
          meta: {
            title: '个人中心'
          },
          children: [
            {
              path: 'history',
              name: 'history',
              component: () => import('@/components/history/HistoryManagement.vue'),
              meta: {
                title: '借阅历史',
                parentRouteName: 'users'
              },
              children: [
                {
                  path: 'historyinfo',
                  name: 'historyinfo',
                  component: BookInfo,
                  meta: {
                    title: '图书信息',
                    parentRouteName: 'history'
                  }
                }
              ]
            },
            {
              path: 'recommend',
              name: 'recommend',
              component: () => import('@/components/recommend/RecommendManagement.vue'),
              meta: {
                title: '个人推荐',
                parentRouteName: 'users'
              },
              children: [
                {
                  path: 'recommendinfo',
                  name: 'recommendinfo',
                  component: BookInfo,
                  meta: {
                    title: '图书信息',
                    parentRouteName: 'recommend'
                  }
                }
              ]
            }
          ]
        },
        {
          path: 'datav',
          name: 'datav',
          component: () => import('@/components/datav/DatavManagement.vue'),
          meta: {
            title: '数据大屏'
          }
        },
        {
          path: 'books',
          name: 'books',
          component: RouterView,
          meta: {
            title: '全部书籍'
          },
          children: [
            {
              path: 'booksearch',
              name: 'booksearch',
              component: () => import('@/components/books/BookSearch.vue'),
              meta: {
                title: '图书检索'
              },
              children: [
                {
                  path: 'booksearchinfo',
                  name: 'booksearchinfo',
                  component: BookInfo,
                  meta: {
                    title: '图书信息',
                    parentRouteName: 'booksearch'
                  }
                }
              ]
            },
            {
              path: 'newbook',
              name: 'newbook',
              component: () => import('@/components/books/NewBook.vue'),
              meta: {
                title: '新书速递'
              },
              children: [
                {
                  path: 'newbookinfo',
                  name: 'newbookinfo',
                  component: BookInfo,
                  meta: {
                    title: '图书信息',
                    parentRouteName: 'newbook'
                  }
                }
              ]
            },
            {
              path: 'popularbook',
              name: 'popularbook',
              component: () => import('@/components/books/PopularBook.vue'),
              meta: {
                title: '热门书籍'
              },
              children: [
                {
                  path: 'popbookinfo',
                  name: 'popbookinfo',
                  component: BookInfo,
                  meta: {
                    title: '图书信息',
                    parentRouteName: 'popularbook'
                  }
                }
              ]
            },
            {
              path: 'bookclass',
              name: 'bookclass',
              component: () => import('@/components/books/BookClass.vue'),
              meta: {
                title: '图书分类'
              },
              children: [
                {
                  path: 'bookclassinfo',
                  name: 'bookclassinfo',
                  component: BookInfo,
                  meta: {
                    title: '图书信息',
                    parentRouteName: 'bookclass'
                  }
                }
              ]
            }
          ]
        },
        {
          path: 'bookinfo',
          name: 'bookinfo',
          component: BookInfo,
          meta: {
            title: '图书信息'
          }
        }
      ]
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/login',
      name: 'login',
      meta: {
        // noAuth: true代表这个页面不需要拦截
        noAuth: true
      },
      component: () => import('../views/LoginView.vue')
    }
  ]
})

//路由前置守卫，验证用户身份，检查权限
//to 即将进入目标路由对象，包含路径、参数、查询参数等
//from 当前导航正要离开的路由对象，包含当前的路由信息
//next 函数，用于控制导航行为，他可以接受一个参数，用于指定导航的目标路由
router.beforeEach((to, from, next) => {
  if (to.meta.noAuth || userinfoStore.authFromLocal) {
    next()
  } else {
    router.push('/login')
  }
})

export default router
