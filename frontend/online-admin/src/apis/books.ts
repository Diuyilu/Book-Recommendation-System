import { get, post } from './api'

// export const getBookInfoAPI = (data) => get('/teacher_portrait/get_book_info', data)
export const getBookInfoAPI = () => get('/api/api/get_book_info')
export const searchBookInfoAPI = (data) => post('/api/api/search_book_info', data)
export const getBookInfoByIdAPI = (data) => post('/api/api/get_book_info_by_id', data)
export const getNewBookInfoAPI = () => get('/api/api/get_new_book_info')
export const getPopBookInfoAPI = () => get('/api/api/get_pop_book_info')
export const getBookLabelAPI = () => get('/api/api/get_book_label')
export const getBookByLabelAPI = (data) => post('/api/api/get_book_by_label', data)

// 书籍数据结构
export interface BookData {
  db_id: string
  book_title: string
  author: string
  press: string
  content_validity: string
  publication_year: string
}
