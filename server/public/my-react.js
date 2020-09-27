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
        const ITEM = ["a make","a model","a mean age","a mean mileage" ];
        return (
            <tr>
            <td>{ITEM[0]}</td>
            <td>{ITEM[1]}</td>
            <td>{ITEM[2]}</td>
            <td>{ITEM[3]}</td>
            </tr>
        );
    }
}

class SinglePage extends React.Component{
    constructor(props){
        super(props);
    }

    render(){
        const listItems = this.props.page.map((car) => <SingleItem key={car[0]} make ={car[0]}/>);
        return(
            <table className="my-table">
                <thead>
                    <tr className="my-tr">
                        <th className="my-th">Make</th>
                        <th className="my-th">Model</th>
                        <th className="my-th">Mean Age (Years)</th>
                        <th className="my-th">Mean Mileage (Miles)</th>
                    </tr>
                </thead>
                <tbody>
                    {listItems}
                </tbody>
            </table>
        );

    }
}

class PageControl extends React.Component{
    constructor(props){
        super(props);
    }

    render(){
        return(<div className="PageControl">
            Begining Previous Next End
        </div> );
    }

}

class SortControl extends React.Component{
    constructor(props){
        super(props);
    }

    render(){
        return(<div>
            sort by: Mean Mileage, Mean Age, Model, Make
        </div> );
    }

}

class PagedEOLControl extends React.Component{
    constructor(props){
        super(props);
    }

    render(){

        const page = [['VW','Golf','11','55'],['Ford','Focus','10','56']];

        return(
            <div>
                <h1>Cars Taken Off Road</h1><br/>
                <SortControl/><br/>
                <SinglePage page={page}/>
                <PageControl/>
            </div>
        );
    }

}
