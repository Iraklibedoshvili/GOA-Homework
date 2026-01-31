import Header from "./header";
let haspremium=true
function App(){
    return(
        <div>
            <Header/>
            <Footer/>
            {haspremium ? <p>you have premium</p> : <p>you dont have premium</p>}
            {haspremium && <p>you have premium</p>}
        </div>
    )
}