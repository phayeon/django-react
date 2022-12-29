import { server, webcrawler, nlp } from '../../context'

const CrawlerService = { navermovieGet, movieReviewPost }

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

async function navermovieGet(){
    const res = fetch(`${server}${webcrawler}naver-movie-get`)
    .then(handleResponse)
    .then(data => JSON.stringify(data))
    .catch((error) => {
        alert('error :::: '+error);
    });
    return Promise.resolve(res);
} 

async function movieReviewPost(review_text){
    const requestOption = {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(review_text)
}
    const res = fetch(`${server}${nlp}movie-review-post`, requestOption)
    .then(handleResponse)
    .then(data => JSON.stringify(data))
    .catch((error) => {
        alert('error :::: '+error);
    });
    return Promise.resolve(res);
} 

export default CrawlerService