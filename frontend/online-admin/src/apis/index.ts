import axios, { AxiosError } from 'axios'
import type { AxiosRequestConfig } from 'axios'
import { ElMessage, ElLoading } from 'element-plus'
export const httpInstance = axios.create()
export type BkResponse = {
  data: any
  code: number
  massage: string
  succeed: true
}

// 设置请求根路径
httpInstance.defaults.baseURL = import.meta.env.VITE_BASEURL

//配置响应拦截器
export const $http = async (config: AxiosRequestConfig) => {
  const loadingInstance = ElLoading.service()
  try {
    const axiosResponse = await httpInstance<BkResponse>(config)
    const bkResponse = axiosResponse.data

    if (!bkResponse?.succeed) {
      let errTitle: string = 'Error'
      if (bkResponse.code === 401) {
        errTitle = 'Unauthorized'
        ElMessage.error('未授权')
        //...
      } else if (bkResponse.code === 403) {
        errTitle = 'Forbidden'
        ElMessage.error('禁止访问')
      } else if (bkResponse.code === 500) {
        errTitle = 'Internal Server Error'
        ElMessage.error('服务器错误')
      } else {
        errTitle = 'Unknown'
      }
      const err = new Error(bkResponse?.massage || 'Unknown')
      err.name = errTitle
      throw err
    }
    return bkResponse
  } catch (err) {
    if (err instanceof AxiosError) {
      ElMessage.error('网络错误')
    }
    throw err
  } finally {
    loadingInstance.close()
  }
}
