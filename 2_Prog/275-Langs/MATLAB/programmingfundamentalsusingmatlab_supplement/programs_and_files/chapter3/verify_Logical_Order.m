% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
%
% verify_Logical_Order.m
%
% Verifying the order of logical operations.
%



disp('What if the OR is done first? It would look like this.');
for a=0:1
    for b=0:1
        for c=0:1
            for d=0:1
                disp(sprintf('%d | %d & %d | %d  becomes   %d & %d  becomes  %d, instead of %d', ...
                    a, b, c, d, a | b, c | d, ((a | b) & (c | d)), (a | b & c | d)));
            end
        end
    end
end
disp(' ');
disp(' ');

disp('What if AND and OR had the same precedence? It would look like this.');
for a=0:1
    for b=0:1
        for c=0:1
            for d=0:1
                disp(sprintf('%d | %d & %d | %d  becomes   %d & %d | %d becomes  %d | %d  becomes %d, instead of %d', ...
                    a, b, c, d, (a | b), c, d, ((a | b) & c), d, (((a | b) & c) | d), (a | b & c | d)));
            end
        end
    end
end
disp(' ');
disp(' ');


disp('The AND is done first. (this works)');

for a=0:1
    for b=0:1
        for c=0:1
            for d=0:1
                disp(sprintf('%d | %d & %d | %d  becomes   %d | %d | %d  becomes  %d', ...
                    a, b, c, d, a, b & c, d, (a | b & c | d)));
            end
        end
    end
end

