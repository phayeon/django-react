import { strokeCheck } from "../api"

const Stroke = () => {

    const strokeClick = e => {
        e.preventDefault()
        alert(`뇌졸중 체크 시작`)
        strokeCheck(Request)
    }
    
    return (
    <body>
        <h2>뇌졸중</h2>
        <button onClick={strokeClick}>시작</button><br/>
    </body>

    )
}
export default Stroke