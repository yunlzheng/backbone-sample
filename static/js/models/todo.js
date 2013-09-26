//js/models/todo.js
var app = app || {};

// Todo Model
//-----------
// Our basic ** Todo ** model has 'title', 'order', and 'completed'
app.Todo = Backbone.Model.extend({

    urlRoot: '/api/todo',
    defaults: {
        title: '',
        completed: false
    },

    parse: function(response) {
          response.id = response._id.$oid;
          delete response._id;
          return response;
    },

    toggle: function() {
        this.save({
            completed: !this.get('completed')
        });
    }

});



