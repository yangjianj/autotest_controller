var Home = Vue.extend({
    template: '<div><h1>Home</h1><p>{{msg}}</p></div>',
    data: function() {
        return {
            msg: 'Hello, vue router!'
        }
    }
});

var About = Vue.extend({
    template: '<div><h1>About</h1><p>This is the tutorial about vue-router.</p></div>'
});

const routes = [
{path:'/home',name:'r_name1',component:Home},
{path:'/form',name:'r_name2',component:form},
{path:'/about_out',name:'r_name3',component:About_out},
{path:'/ele_css',name:'r_n',component:conn1},
];

const router1 = new VueRouter({routes});

const app= new Vue({
	el: "#app",
	router:router1,
	methods:{
		diyfun:function(){
			myfun()
		}
	}
	});