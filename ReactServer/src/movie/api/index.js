import axios from 'axios'
const server = `http://localhost:8000`
const dlearn = `/movie/theater_tickets/`
export const strokeCheck = req => axios.get(`${server}/movie/theater_tickets/stroke`, req)
export const irisGet = req => axios.get(`${server}/movie/theater_tickets/irisget`, req)
export const irisPost = req => axios.post(`${server}/movie/theater_tickets/irispost`, req)
export const fashionPost = post_num => axios.post(`${server}/movie/theater_tickets/fashion?post_num=${post_num}`, {post_num})
export const fashionGet = get_num => axios.get(`${server}/movie/theater_tickets/fashion?get_num=${get_num}`)
const dlearnService = { numberPost }

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
async function numberPost(num){
    const requestOption = {
        method: "POST",
        headers: { "Content-Type" : "application/json"},
        body: JSON.stringify(num)
    }
    fetch(`${server}${dlearn}number`, requestOption)
    .then(handleResponse)
    .then(data => {
        alert('결과: '+JSON.stringify(data))
    })
    .catch((error) => {
        alert('error :::: '+error);
    });
}

export default dlearnService