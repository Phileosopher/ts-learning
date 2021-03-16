% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_6_1.m

    filename1 = 'myemails.txt';
        % Open files, check that it worked.
    infile = fopen(filename1, 'r');
    if (infile < 0)
        error('Could not open the input file');
        return
    end
    % Read the whole file in.
    temp = fgets(infile);
    linecount = 0;
    while (ischar(temp))
        % disp(temp);
        linecount = linecount + 1;
        lines{linecount} = temp;
        temp = fgets(infile);
    end
    fclose(infile);

    % Look through the lines, isolating the subjects
    LF = 10; % linefeed, end of line
    em = 0; % email index
    for k=1:length(lines)
        temp = lines{k};
        % Note the space after the m in the next line
        foundStatus = strfind(temp, 'From ');
        if ((~isempty(foundStatus)) && (foundStatus == 1))
            % This is the start of a new message
            header = true;
            if (em > 0)
                % This is not our first email, 
                % so remember stop
                email(em).stopLine = k-1;
            end
            em = em + 1;
            email(em).startLine = k;
        end
        if ((temp(1) == LF) && (header))
            % Found start of message body
            header = false;
            email(em).startBody = k;
        end
        foundStatus = strfind(temp, 'Subject');
        if ((~isempty(foundStatus)) && (foundStatus == 1) ...
            && header)
            % Found the subject 
            % If input is malformed, em could be 0.
            email(em).subjectIndex = k;
        end
    end
    % Remember last stop line
    email(em).stopLine = k;

    % Put all subjects together
    for k=1:length(email)
        si = email(k).subjectIndex;
        subjects{k} = lines{si};
    end
    % Sort the subjects
    [sorted, indices] = sort(subjects);
    
    % Print e-mails in sorted order
    % This could be done to a file.
    for m=1:length(indices)
        % Show emails in sorted order
        em = indices(m);
        for k=email(em).startLine:email(em).stopLine
            % On the screen, this prints an extra LF 
            % after each line
            disp(lines{k});
        end
    end 
