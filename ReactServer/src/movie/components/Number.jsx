import dlearnService from "../api"
import { useState } from "react"

const Number = () => {
    const [inputs, setInputs] = useState({})
    const {num} = inputs
    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target 
        setInputs({...inputs, [name]: value})
    }

    const postClick = e => {
        e.preventDefault()
        dlearnService.numberPost(num)
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }

    return (
    <>
        <h2> 숫자 입력</h2>
        <form method="post">
        <input type="text" className="box" name="num" placeholder="숫자 입력" onChange={onChange}></input>
        <button onClick={postClick}>Click</button><br/>
        </form>
    </>
    )
}
export default Number