const department={
    template:`
<div>

<button type="button" 
class="btn btn-primary m-2 fload-end"
data-bs-toggle="modal"
data-bs-target="#exampleModal"
@click="addClick()">
    Add Department
</button>

<table class="table table-striped">
<thead>
    <tr>
        <th>
            DepartmentId
        </th>
        <th>
            DepartmentName
        </th>
        <th>
            Options
        </th>                
    </tr>
</thead>
<tbody>
    <tr v-for="dep in departments">
        <td>{{dep.DepartmentId}}</td>
        <td>{{dep.DepartmentName}}</td>
        <td>
            <button type="button"
            class="btn btn-light mr-1"
            data-bs-toggle="modal"
            data-bs-target="#exampleModal"
            @click="editClick(dep)">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
                <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
                </svg>
            </button>
            <button type="button" @click="deleteClick(dep.DepartmentId)"
            class="btn btn-light mr-1">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash3-fill" viewBox="0 0 16 16">
                <path d="M11 1.5v1h3.5a.5.5 0 0 1 0 1h-.538l-.853 10.66A2 2 0 0 1 11.115 16h-6.23a2 2 0 0 1-1.994-1.84L2.038 3.5H1.5a.5.5 0 0 1 0-1H5v-1A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5Zm-5 0v1h4v-1a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5ZM4.5 5.029l.5 8.5a.5.5 0 1 0 .998-.06l-.5-8.5a.5.5 0 1 0-.998.06Zm6.53-.528a.5.5 0 0 0-.528.47l-.5 8.5a.5.5 0 0 0 .998.058l.5-8.5a.5.5 0 0 0-.47-.528ZM8 4.5a.5.5 0 0 0-.5.5v8.5a.5.5 0 0 0 1 0V5a.5.5 0 0 0-.5-.5Z"/>
                </svg>
            </button>
        </td>                
    </tr>
</tbody>
</table>

<div class="modal fade" id="exampleModal" tabindex="-1"
    aria-labelledby="exampleModalLabel" aria-hidden="true">
<div class="modal-dialog modal-lg modal-dialog-centered">
<div class="modal-content">
    <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">{{modalTitle}}</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"
        aria-label="Close"></button>
    </div>

    <div class="modal-body">
        <div class="input-group mb-3">
            <span class="input-group-text">Department Name</span>
            <input type="text" class="form-control" v-model="DepartmentName">
        </div>
    </div>

    <button type="button" @click="createClick()"
    v-if="DepartmentId==0" class="btn btn-primary">
        Create
    </button>

    <button type="button" @click="updateClick()"
    v-if="DepartmentId!=0" class="btn btn-primary">
        Update
    </button>

</div>
</div>
</div>

</div>
`,

data(){
    return{
        departments:[],
        modalTitle:"",
        DepartmentName:"",
        DepartmentId:0
    }
},
methods: {
    refreshData(){
        axios.get(variables.API_URL+"department")
        .then((response)=>{
            this.departments=response.data;
        })
    },
    addClick(){
        this.modalTitle="Add Department";
        this.DepartmentId=0;
        this.DepartmentName="";
    },
    editClick(dep){
        this.modalTitle="Edit Department";
        this.DepartmentId=dep.DepartmentId;
        this.DepartmentName=dep.DepartmentName;
    },
    createClick(){
        axios.post(variables.API_URL+"department",{
            DepartmentName:this.DepartmentName
        })
        .then((response)=>{
            this.refreshData();
            alert(response.data);            
        })
    },
    updateClick(){
        axios.put(variables.API_URL+"department",{
            DepartmentId:this.DepartmentId,
            DepartmentName:this.DepartmentName
        })
        .then((response)=>{
            this.refreshData();
            alert(response.data);            
        })
    },
    deleteClick(id){
        if(!confirm("Are you sure?")){
            return;
        }
        axios.delete(variables.API_URL+"department/"+id)
        .then((response)=>{
            this.refreshData();
            alert(response.data);   
        });
    }
},
mounted:function(){
    this.refreshData();
}}