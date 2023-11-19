import { get, post } from './api'

// export const getBookInfoAPI = (data) => get('/teacher_portrait/get_book_info', data)
export const getBookInfoAPI = () => get('/api/api/get_book_info')
export const searchBookInfoAPI = (data) => post('/api/api/search_book_info', data)
export const getBookInfoByIdAPI = (data) => post('/api/api/get_book_info_by_id', data)
export const getNewBookInfoAPI = () => get('/api/api/get_new_book_info')

// 书籍数据结构
export interface BookData {
  db_id: string
  book_title: string
  author: string
  press: string
  content_validity: string
  publication_year: string
}
