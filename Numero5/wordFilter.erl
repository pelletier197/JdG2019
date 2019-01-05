-module(wordFilter).
-compile(export_all).


	for(0,_) -> 
	   []; 
	   X = string:length(Criteria),
	   
	   for(N,Term) when N > 0 -> 
		   {ok, Word} = io:read("Enter a word : "),
					io:format("The word entered are: ~w~n", 
						  [Word]),
			for(X,T2) ->
				Y = lists:sublist(String, X + 1).
				if 
				  lists:member(hd("+"),Word) -> 
					 io:fwrite("True"); 
				  true -> 
					 io:fwrite("False") 
			    end.
				
			[T2|for(X-1,T2)].
		
	   [Term|for(N-1,Term)]. 
   
	start() -> 
		{ok, Criteria} = io:read("Enter 1 or multiple filter letters followed with <.> : "),
				io:format("The filter you entered is: ~w~n", 
						  [Criteria]),
	   for(2,1).

			
			

		
				  
