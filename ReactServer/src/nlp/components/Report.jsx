import { useState } from "react"
import ReportService from "../api"

const SamsungReport = () => {
    const [text, setText] = useState()

    const onClick = e => {
        e.preventDefault()
        ReportService.reportGet().then(res => {
            const json = JSON.parse(res)
            setText(json['result'])
        })
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }

    return (
    <>
        <h2> Samsung-Report </h2>
        <button onClick={onClick}>추출 시작</button><br/>
        <p>버튼을 클릭하시면, 단어와 빈도수 목록이 출력됩니다.</p>
        <table>
            <thead>
                <tr>
                    <th>단어</th><th>빈도수</th>
                </tr>
            </thead>
            {text && text.map(({단어, 빈도수}) => (
                <tr>
                    <td key={단어}>{단어}</td><td key={빈도수}>{빈도수}</td>
                </tr>
            ))}
        </table>
    </>
    )
}
export default SamsungReport