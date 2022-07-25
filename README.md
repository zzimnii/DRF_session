# DRF_session
프로젝트명: sessionproject
APP: postapp(게시글, 댓글), accounts(사용자)

urls.py (project내부)

	path('', include('postapp.urls')),
	path('api/user/', include('accounts.urls')),
    path('api/user/', include('allauth.urls')),
	post와 달리 사용자와 관련된 url은 api/user/ 경로를 붙임

Postapp-> 게시글, 댓글 CRUD구현

models.py

	Post
		id: pk
		user: fk accounts.User
		title: CharField, 글자수 14자로 제한
		photo: ImageField, post_photo에 업로드됨

	Comment
		id: pk
		post: fk postapp.Post
		user: fk accounts.User
		comment: TextField

serializers.py

	PostSerializer
		user = serializers.ReadOnlyField(source = 'user.nickname')
		    model = Post
        fields = ['id', 'title', 'photo', 'user' ]

	CommentSerializer
		user = serializers.ReadOnlyField(source = 'user.nickname')
        model = Comment
        fields = [ 'id', 'post', 'comment', 'user' ]

	source = 'user.nickname'을 이용하여 user가 설정한 id가 보이도록 함

views.py	->ModelViewSet을 사용해서 CRUD 구현

	PostViewSet
		queryset = Post.objects.all()
   		serializer_class = PostSerializer
		
	CommentViewSet
		queryset = Comment.objects.all()
    serializer_class = CommentSerializer
		
		def get_queryset(self, **kwargs): # Override	: post_id를 받아 해당 게시글과 연결
			post_id = self.kwargs['post_id']
			return self.queryset.filter(post=post_id)
		
	authentication_classes = [BasicAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]를 통해
	로그인하지 않으면 읽기만 가능, 로그인 해야 생성 가능, 본인이 작성한 게시글, 댓글만 삭제, 수정 가능하게 구현
	(permissions.py의 IsOwnerOrReadOnly(permissions.BasePermission)로 구현)

urls.py

	/post	: 게시글 목록 조회, 생성
	/posts/<int:post_id>: 게시글 상세정보 조회	+ 본인 게시글이면 수정, 삭제 가능
	/posts/<int:post_id>/comments	: 해당 게시글의 댓글 목록 조회, 댓글 생성
	/posts/<int:post_id>/comments/<int:comment_id>: 댓글 상세정보 조회 + 본인 댓글이면 수정, 삭제 가능



Accounts-> 회원가입, 로그인

models.py

	User
		id: pk
		name: CharField
		nickname: CharField, unique, user의 id역할
		password: CharField
		email: EmailField, unique

	BaseUserManager를 통해 user를 생성하고 AbstractBaseUser를 상속 받아 model 작성

serializers.py

	UserSerializer
		def create(self, validated_data):
       			user = User.objects.create_user( ...)로 유효한 값인지 확인
		model = User
    fields = ['name', 'nickname', 'password', 'email']

views.py	->ModelViewSet을 사용해서 CRUD 구현

	UserViewSet
		queryset = User.objects.all()
    serializer_class = UserSerializer
	
urls.py

	/api/user/siginup/user : 회원가입
	/api/user/api-auth/login: 로그인
