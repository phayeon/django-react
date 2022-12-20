import dlearnService from "../api"
import { useState } from "react"

const Iris = () => {
    const [inputs, setInputs] = useState({})
    const {sl, sw, pl, pw} = inputs;

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target 
        setInputs({...inputs, [name]: value})
    }

    const onClick = e => {
        e.preventDefault()
        const Request = {sl, sw, pl, pw}
        alert(`입력하신 정보는 \n ${JSON.stringify(Request)} \n 이 맞습니까?`)
        dlearnService.irisPost(Request)
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }

    const getClick = e => {
        e.preventDefault()
        alert(`작업 요청`)
        dlearnService.irisGet(Request)
    }
    
    return (
    <>
        <h2>아이리스 속성 값 입력</h2>
        <button onClick={getClick}>작업 요청</button><br/><br/>
        <input type="text" name="sl" placeholder="꽃받침 길이" onChange={onChange}></input><br/>
        <input type="text" name="sw" placeholder="꽃받침 넓이" onChange={onChange}></input><br/>
        <input type="text" name="pl" placeholder="꽃잎 길이" onChange={onChange}></input><br/>
        <input type="text" name="pw" placeholder="꽃잎 넓이" onChange={onChange}></input>
        <button onClick={onClick}>입력</button>
    </>
    )
}
export default Iris