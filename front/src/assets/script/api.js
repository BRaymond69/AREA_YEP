import axios from 'axios'
/*
let buildToken = () => {
    return localStorage.getItem('token')
}
*/

const axiosGet = axios.create({baseURL:"http://localhost:8080"})

axiosGet.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('token')
        if (token)
            config.headers["Authorization"] = 'Token ' + token
        return config
    },
    (error) => {
        return Promise.reject(error)
    }
)

export default axiosGet