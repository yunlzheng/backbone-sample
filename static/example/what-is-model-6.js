/**
Interacting with the server
*/

GroupModel = Backbone.Model.extend({
	urlRoot:'http://pdflabs.herokuapp.com/api/rest/group',
	defaults:{
		name: '',
		tag: '',
		create_at: ''
	},
	initialize: function(){
		alert("Welcome to this world");
		this.on("change:name", function(model){

			var name = model.get("name");
			alert("change my name to " + name);

		});
	}

});

var group = new GroupModel();

groupDetails = {
	name:'臆想',
	tag:'yx'
};

group.save(groupDetails,{

	success:function(group){
		alert(group);
	}

});

