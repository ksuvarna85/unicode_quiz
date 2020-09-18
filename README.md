Student Teacher Quiz CRUD with User Authentication
An app where student and teachers can register/log in. Teachers can create a quiz on a subject and can view students that have given it and see their markd. Student can take a quiz (only once) and can see the correct answers and their marks

ABOUT THE PROJECT
User Authentication :
The accounts app manages all tasks related to registration, login, logout. It has 3 models: User, Student, Teacher. All these models are derived from AbstractBaseUser as it helps us in getting complete control over the model. The models use 'Email' as the 'Username' field and all the models are accessible in the Django Admin page. The registeration form is seperate for students and teachers and the whole project can be authorised using is_student and is_teacher boolean variables along with ROLE (STUDENT or TEACHER). 

CRUD APP
The CRUD app is regulated using is_student, is_teacher and is_authenticated booleans. There is a create-quiz form where teachers can name the quiz subject/topic and the number of questions in that quiz. They are then directed to the add-questions page where they can add questions with options and the correct answer and then submit the quiz for students. They can also update the quiz questions by going to the update/<quiz_id> page and updating the questions. They can delete the quiz in the same way by going to delete/<quiz_id> url.
