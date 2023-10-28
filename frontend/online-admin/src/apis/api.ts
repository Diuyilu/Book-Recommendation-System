import axios from 'axios'
import Router from '../router/index'

export function post(url: string, data?: any) {
  return new Promise<any>((resolve, reject) => {
    axios.post(url, data).then(
      (res) => {
        // console.log(res)
        if (res.data.status === -1) {
          Router.push('/login')
        } else {
          resolve(res.data)
        }
      },
      (err) => {
        reject(err)
      }
    )
  })
}

export function get(url: string, options?: any) {
  console.log('url:' + url)
  let params = {}
  if (options !== undefined) {
    params = options.params || {}
  }
  return new Promise<any>((resolve, reject) => {
    axios.get(url, { params }).then(
      (res) => {
        if (res.data.status === -1) {
          Router.push('/login')
        } else {
          resolve(res.data)
        }
      },
      (err) => {
        reject(err)
      }
    )
  })
}

export function put(url: string, params: any) {
  return new Promise<any>((resolve, reject) => {
    axios
      .put(url, params)
      .then(
        (res) => {
          if (res.data.status === -1) {
            Router.push('/login')
          } else {
            resolve(res.data)
          }
        },
        (err) => {
          reject(err.data)
        }
      )
      .catch((err) => {
        reject(err.data)
      })
  })
}
