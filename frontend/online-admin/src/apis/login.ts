import { $http } from '.'
import qs from 'qs'

// 登录接口
export const loginApi = (data: { password: string; username: string }) => {
  return $http({
    method: 'POST',
    url: '/api/login',
    headers: { 'content-type': 'application/x-www-form-urlencoded' },
    data: qs.stringify(data)
  })
}
