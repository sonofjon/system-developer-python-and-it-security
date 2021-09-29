var employee = {
    name: "Mary Smith",
    job: "Programmer",
    age: 32,
    report: function(){
        alert("Name is " + this.name + ", Job is " + this.job + ", Age is " + this.age + ".")
    },
    lastName: function(){
        nameLast = this.name.split(' ')[1];
        alert("Last name is " + nameLast + ".")
    }
}