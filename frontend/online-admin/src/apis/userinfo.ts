// import { $http } from '.'
// import qs from 'qs'

// // 获取用户信息
// export const getUserinfoApi = () => {
//   return $http({
//     method: 'GET',
//     url: '/api/get_user_info',
//     headers: { 'content-type': 'application/x-www-form-urlencoded' },
//     withCredentials: true
//   })
// }
import { get } from './api'

export const getUserinfoApi = () => get('/api/api/get_user_info')
