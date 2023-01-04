import { server, dlearn } from '../../context'

const dlearnService = { fashionGet, fashionPost, strokeCheck, irisPost, irisGet, aitraderPost }

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

async function fashionPost(post_num){
    const requestOption = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(post_num)
    }
    fetch(`${server}${dlearn}fashion`, requestOption)
    .then(handleResponse)
    .then(data => {
        alert('결과: '+JSON.stringify(data))
    })
    .catch((error) => {
        alert('error :::: '+error);
    });
}

async function fashionGet(get_num){
    fetch(`${server}${dlearn}fashion?get_num=${get_num}`)
    .then(handleResponse)
    .then(data => {
        alert('결과: '+JSON.stringify(data))
    })
    .catch((error) => {
        alert('error :::: '+error);
    });
} 

async function strokeCheck(){
    fetch(`${server}${dlearn}stroke`)
    .then(handleResponse)
    .then(alert('결과 : 출력 성공'))
    .catch((error) => {
        alert('error :::: '+error);
    });
} 

async function irisPost(sl, sw, pl, pw){
    const requestOption = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(sl, sw, pl, pw)
    }
    fetch(`${server}${dlearn}irispost`, requestOption)
    .then(handleResponse)
    .then(data => {
        alert(JSON.stringify(data))
    })
    .catch((error) => {
        alert('error :::: '+error);
    });
}

async function irisGet(){
    fetch(`${server}${dlearn}irisget`)
    .then(handleResponse)
    .then(
        alert('작업 성공')
    )
    .catch((error) => {
        alert('error :::: '+error);
    });
}

async function aitraderPost(date){
    const requestOption = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(date)
    }
    const res = await fetch(`${server}${dlearn}aitrader-post`, requestOption)
    .then(handleResponse)
    .then(data => JSON.stringify(data))
    .catch((error) => {
        alert('error :::: '+error);
    });
    return Promise.resolve(res);
} 

export default dlearnService