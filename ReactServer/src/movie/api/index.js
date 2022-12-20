const server = `http://localhost:8000`
const dlearn = `/movie/theater_tickets/`
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