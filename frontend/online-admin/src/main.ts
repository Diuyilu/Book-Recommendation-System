import './assets/main.scss'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import 'element-plus/dist/index.css'
import axios from 'axios'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

const app = createApp(App)

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

// app.use(createPinia())
// app.use(router)

// app.mount('#app')

async function asyncRegister() {
  const createPinia = (await import('pinia')).createPinia
  app.use(createPinia())
  const router = (await import('@/router')).default
  app.use(router)

  app.mount('#app')
}

asyncRegister()
