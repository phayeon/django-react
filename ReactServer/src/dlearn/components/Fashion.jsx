import dlearnService from "../api"
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
        dlearnService.fashionPost(post_num)
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }
    
    const getClick = e => {
        e.preventDefault()
        dlearnService.fashionGet(get_num)
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }
    
    return (
    <>
        <h2> 의류 번호 입력</h2>
        <form method="post">
        <input type="text" className="box" name="post_num" placeholder="숫자 입력" onChange={onChange}></input>
        <button onClick={postClick}>postClick</button><br/>
        </form>
        <form method="get">
        <input type="text" className="box" name="get_num" placeholder="숫자 입력" onChange={onChange}></input>
        <button onClick={getClick}>getClick</button>
        </form>
    </>
    )
}
export default Fashion