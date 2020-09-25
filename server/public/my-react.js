class MyComponent extends React.Component{
    constructor(props){
        super(props);
    }
    render(){
        return (<h1>OK</h1>);
    }
}


class SingleItem extends React.Component{
    constructor(props){
        super(props);
    }
    render(){
        return (<tr><td>a make</td><td>a model</td><td>mean age</td>mean mileage<td></td></tr>);
    }
}

class SinglePage extends React.Component{
    constructor(props){
        super(props);
    }

    render(){
        const page = [['VW','Golf','11','55'],['Ford','Focus','10','56']];
        const listItems = page.map((car) => <SingleItem make ={car[0]}/>);
        return(listItems);
    }
}
