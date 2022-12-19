import '../styles/SignUp.css'
import { useState } from 'react'
import { userLogin } from '../api'

const SignUp = () => {
    const [inputs, setInputs] = useState({})
    const {email, nickname, password} = inputs;

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target 
        setInputs({...inputs, [name]: value})
    }
    const onClick = e => {
        e.preventDefault()
        const Request = {email, nickname, password}
        alert(`${JSON.stringify(Request)}`)
        userLogin(Request)
    }

    return (<>
        E-MAIL: <input type="text" name="email" onChange={onChange}/><br/>
        NICKNAME: <input type="text" name="nickname" onChange={onChange}/><br/>
        PASSWORD: <input type="text" name="password" onChange={onChange}/><br/>
        <button onClick={onClick}> 회원가입 </button>
    </>)
}
export default SignUp