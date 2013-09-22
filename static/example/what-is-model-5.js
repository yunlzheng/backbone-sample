/**
Listening for changes to the model
*/

Person = Backbone.Model.extend({

	defaults:{
		name: 'Fetus',
		age: 0,
		child: ''
	},
	initialize: function(){
		alert("Welcome to this world");
		this.on("change:name", function(model){

			var name = model.get("name");
			alert("change my name to " + name);

		});
	},
	adopt: function( newchildname ){
		this.set({ child: newchildname });
	}

});

var person = new Person({name:"Thomas", age:67, child: 'Ryan'});
person.set({name : 'Stewie Griffih'});

var age = person.get("age");
var child = person.get("child");
var name = person.get("name");
console.log("name"+name);
console.log("age:"+age);
console.log("child:"+child);