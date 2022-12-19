import { fashionPost, fashionGet } from "../api"
import { useState } from "react"

const Fashion = () => {
    const [inputs, setInputs] = useState({})
    const {get_num, post_num} = inputs
    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target 
        setInputs({...inputs, [name]: value})
    }

    const postClick = e => {
        e.preventDefault()
        alert(`입력하신 정보는 \n ${JSON.stringify(post_num)} \n 이 맞습니까?`)
        fashionPost(post_num)
        .then((res) => {
            alert(`옷의 카테고리 : ${JSON.stringify(res.data.result)}`)
        })
        .catch((err) => {
            console.log(err)
            alert('잘못된 접근입니다.')
        })
    }

    const getClick = e => {
        e.preventDefault()
        fashionGet(get_num)
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }
    
    return (
    <body>
        <h2> 의류 번호 입력</h2>
        <form method="post">
        <input type="text" name="post_num" placeholder="숫자 입력" onChange={onChange}></input>
        <button onClick={postClick}>postClick</button><br/>
        </form>
        <form method="get">
        <input type="text" name="get_num" placeholder="숫자 입력" onChange={onChange}></input>
        <button onClick={getClick}>getClick</button>
        </form>
    </body>
    )
}
export default Fashion