import { useState } from "react"
import { userLogin } from '../api'
import { useNavigate } from 'react-router-dom'

export default function Login(){
    const [inputs, setInputs] = useState({})
    const {email, nickname, password} = inputs;
    const navigate = useNavigate()

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target 
        setInputs({...inputs, [name]: value})
    }
    const onClick = e => {
        e.preventDefault()
        const Request = {email, nickname, password}
        alert(`사용자 정보는 ${JSON.stringify(Request)} 이 맞습니까?`)
        userLogin(Request)
        .then((res) => {
            localStorage.setItem('loginUser', JSON.stringify(res.data))
            alert(`response is ${localStorage.getItem('loginUser')}`)
            navigate("/home")
        })
        .catch((err) => {
            console.log(err)
            alert('아이디와 비밀번호를 다시 입력해주세요')
        })
    }

    return (
    <>
        Email: <input type="text" name="email" onChange={onChange} /><br/>
        Nickname: <input type="text" name="nickname" onChange={onChange} /><br/>
        PASSWORD: <input type="text" name="password" onChange={onChange} /><br/>
        <button onClick={onClick}> 로그인 </button>

    
    </>
)}