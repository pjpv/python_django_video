import env from '../config/env'

export default {
    method: 'get',
    // 基础url前缀
    baseURL: env === 'production' ? '/api' : 'http://192.168.0.88:8000/api',
    // 请求头信息
    headers: {
        'Content-Type': 'application/json;charset=UTF-8'
    },
    // 参数
    data: {},
    // 设置超时时间
    timeout: 10000,
    // 携带凭证
    withCredentials: true,
    // 返回数据类型
    responseType: 'json'
}