import { server, blog } from '../../context'

import axios from 'axios'
export const userLogin = req => axios.post(`http://localhost:8000/blog/auth/login`, req)

const BlogService = {
    blogPost
}

function handleResponse(response){ 
    return response.text()
        .then(text =>{
            const data = text && JSON.parse(text)
            if(!response.ok){
                if(response.status === 401){
                    window.location.reload()
                }
                const error = (data && data.message) ||
                    response.statusText
                return Promise.reject(error)
            }
            return data
        })
    }

async function blogPost(){
    const res = fetch(`${server}${blog}user-create`)
    .then(handleResponse)
    .then(data => JSON.stringify(data))
    .catch((error) => {
        alert('error :::: '+error);
    });
    return Promise.resolve(res);
} 

export default BlogService