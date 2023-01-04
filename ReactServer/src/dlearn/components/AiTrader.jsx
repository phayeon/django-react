import { useState } from "react"
import dlearnService from "../api"

const AiTrader = () => {
    const [text, setText] = useState()
    const [inputs, setInputs] = useState({})
    const {date} = inputs

    const onClick = e => {
        e.preventDefault()
        dlearnService.aitraderPost(date).then(res => {
            const json = JSON.parse(res)
            setText(json['result'])
        })
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target 
        setInputs({...inputs, [name]: value})
    }

    return (
    <>
        <h2> AiTrader-Report </h2>
        <input type="text" className="box" name="date" placeholder="예)230104" onChange={onChange}/>
        <button onClick={onClick}>추출 시작</button><br/>
        <p>버튼을 클릭하시면, 예측가가 출력됩니다.</p>
        <table>
            <thead>
                <tr>
                    <th>종가</th><th>예측가</th>
                </tr>
            </thead>
            {text && text.map(({종가, 예측가}) => (
                <tr>
                    <td key={종가}>{종가}</td><td key={예측가}>{예측가}</td>
                </tr>
            ))}
        </table>
    </>
    )
}
export default AiTrader