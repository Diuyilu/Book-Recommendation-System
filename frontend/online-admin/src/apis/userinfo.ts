import { $http } from '.'
import qs from 'qs'

// 获取用户信息
export const getUserinfoApi = () => {
  return $http({
    method: 'GET',
    url: '/api/login',
    headers: { 'content-type': 'application/x-www-form-urlencoded' },
  })
}
