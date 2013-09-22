/**
Setting model defaults
*/

Person = Backbone.Model.extend({

	defaults:{
		name: 'Fetus',
		age: 0,
		child: ''
	},
	initialize: function(){
		alert("Welcome to this world");
	}

});

var person = new Person({name:"Thomas", age:67, child: 'Ryan'});

/**the other way can set ttribute afterwards*/
/*var person2 = new Person();
person2.set({name: 'Thomas', age: 67});*/

var age = person.get("age");
var child = person.get("child");
var name = person.get("name");

console.log(age+" "+name+" "+child);