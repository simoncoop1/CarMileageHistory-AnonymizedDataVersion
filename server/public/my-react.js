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
            <td>{this.props.make}</td>
            <td>{this.props.model}</td>
            <td>{this.props.avMileage}</td>
            <td>{this.props.avAge}</td>
            </tr>
        );
    }
}

class SinglePage extends React.Component{
    constructor(props){
        super(props);
    }

    render(){
        const listItems = this.props.page.map((car) => <SingleItem key={car['make']+car['model']} make ={car['make']} model={car['model']} avMileage={Math.round(car['mA'])} avAge={Number(car['mM'].toPrecision(3))}/>);
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
        this.handleClick = this.handleClick.bind(this);
    }

    handleClick(e){
        this.props.onPageChange(this.props.currentPage+1);
    }

    render(){

        return(<div className="PageControl">
            Begining Previous Next End <a href='#' onClick={this.handleClick}>next</a>
        </div> );
    }

}

class SortControl extends React.Component{
    constructor(props){
        super(props);
        this.handleSortMileage = this.handleSortMileage.bind(this);
        this.handleSortAge = this.handleSortAge.bind(this);
        this.handleSortModel = this.handleSortModel.bind(this);
        this.handleSortMake = this.handleSortMake.bind(this);
    }

    handleSortMileage(e){
        e.preventDefault();
        this.props.onSortChange("mileage");
    }

    handleSortAge(e){
        e.preventDefault();
        this.props.onSortChange("age");
    }
    handleSortMake(e){
        e.preventDefault();
        this.props.onSortChange("make");
    }
    handleSortModel(e){
        e.preventDefault();
        this.props.onSortChange("model");
    }

    render(){

        return(<div>
            sort by: 
            <a className={this.props.sort == 'mileage'?"highlight-sort":""} href='#' onClick={this.handleSortMileage}>Mean Mileage</a>, 
            <a className={this.props.sort == "age" ? "highlight-sort":""} href='#' onClick={this.handleSortAge}>Mean Age</a>,
            <a className={this.props.sort == "model" ? "highlight-sort":""} href='#' onClick={this.handleSortModel}>Model</a>, 
            <a className={this.props.sort == "make"?"highlight-sort":""} href='#' onClick={this.handleSortMake}>Make</a>
            </div> );
    }

}

class PagedEOLControl extends React.Component{
    constructor(props){
        super(props);
        this.handlePageChange = this.handlePageChange.bind(this);
        this.handleSortChange = this.handleSortChange.bind(this);
        this.state = {
            error: null,
            isLoaded:false,
            items:[],
            page:0,
            itemsPerPage:40,
            sortType:'mileage',
        };        
    }

    componentDidMount(){
        fetch("off-road-by-make-40-react.json")
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        items: result,
                    });
                    console.log(result.length);
                    
                }, 
                // Note: it's important to handle errors here
                // instead of a catch() block so that we don't swallow
                // exceptions from actual bugs in components.
                (error) => {
                    this.setState({
                        isLoaded: true,
                        error
                    });
                }
            )
    }

    handlePageChange(page){
        this.setState({page:page});
    }

    handleSortChange(sort){
        this.setState({sortType:sort});
        
        
        if(sort == 'age'){

            this.state.items.sort(function(a, b) {
                return parseFloat(a.mA) - parseFloat(b.mA);
            });
        }
        else if(sort == 'mileage'){
            this.state.items.sort(function(a, b) {
                return parseFloat(a.mM) - parseFloat(b.mM);
            });
        }
        else if(sort == 'model'){
            this.state.items.sort(function(a, b) {
                return a.model.localeCompare(b.model);
            });
        }
        else if(sort == 'make'){
            this.state.items.sort(function(a, b) {
                return a.make.localeCompare(b.make);
            });
        }
    }

    render(){ 
        const si = this.state.page*40;
        const ei = si + 40;
        const page = this.state.items.slice(si,ei);

        const pageCount = Math.ceil(this.state.items.length / this.state.itemsPerPage);

        return(
            <div className ="my-style">
                <h1>Cars Taken Off Road</h1><br/>
                  <SortControl sort={this.state.sortType} onSortChange={this.handleSortChange} /><br/>
                <SinglePage page={page}/>
                <PageControl pageCount={pageCount} currentPage={this.state.page} onPageChange={this.handlePageChange}/>
            </div>
        );
    }

}  
