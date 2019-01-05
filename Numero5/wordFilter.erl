-module(wordFilter).
-compile(export_all).


	for(0,_) -> 
	   []; 
	   X = string:length(Criteria),
	   
	   for(N,Term) when N > 0 -> 
		   {ok, Word} = io:read("Enter a word : "),
					io:format("The word entered are: ~w~n", 
						  [Word]),
			io:fwrite("True").

		
	   [Term|for(N-1,Term)]. 
   
	start() -> 
		{ok, Criteria} = io:read("Enter 1 or multiple filter letters followed with <.> : "),
				io:format("The filter you entered is: ~w~n", 
						  [Criteria]),
	   for(2,1).

			
			

		
				  
