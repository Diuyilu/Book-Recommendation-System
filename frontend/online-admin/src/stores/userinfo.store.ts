import { httpInstance } from '@/apis'
import router from '@/router'
import { defineStore } from 'pinia'

export const useUserInfoStore = defineStore('userinfo-store', () => {
  //将token存入浏览器本地存储localStorage中，把TOKEN放在请求头部AUTHORIZATION字段中
  const setAuth = (token: string) => {
    httpInstance.defaults.headers.common.Authorization = token
    localStorage.setItem('token', token)
  }
  //判断用户是否登录
  const authFromLocal = () => {
    const token = localStorage.getItem('token')
    if (token) {
      setAuth(token)
      return true
    }
    return false
  }
  //将TOKEN从请求头部清除，并从本地浏览器localStorage中清除，并强制跳转登录页面
  const removeAuth = () => {
    delete httpInstance.defaults.headers.common.Authorization
    localStorage.removeItem('token')
    router.push('/login')
  }
  return {
    setAuth,
    authFromLocal,
    removeAuth
  }
})
