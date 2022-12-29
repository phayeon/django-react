import '../styles/UserList.css'

export default function ListForm({list}){
    return (
    <>
         <h2> 유저 목록 </h2>
         <table className='UserList'>
            <thead>
               <tr>
                  <th>blog_userid</th>
                  <th>email</th>
                  <th>nickname</th>
                  <th>password</th>
               </tr>
            </thead>
         {list && list.map(({blog_userid, email, nickname, password}) => (
                <tbody>
                  <tr>
                    <td key={blog_userid}>{blog_userid}</td>
                    <td key={email}>{email}</td>
                    <td key={nickname}>{nickname}</td>
                    <td key={password}>{password}</td>
                  </tr>
                </tbody>
            ))}
         </table>
    </>
)}