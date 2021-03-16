% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_6_3_decode.m

    filename1 = 'somebinaryfile.txt';
    filename2 = 'somebinaryfile2';
    base64 = strcat('ABCDEFGHIJKLMNOPQRSTUVWXYZ', ...
        'abcdefghijklmnopqrstuvwxyz0123456789+/=');
    % Open files, check that it worked.
    infile = fopen(filename1, 'r');
    outfile = fopen(filename2, 'w');
    if ((infile < 0) || (outfile < 0))
        error('Could not open the files');
        return
    end

    % Process the input
    binvals2 = [1, 2, 4, 8, 16, 32, 64, 128];
    [ch, notdone] = fscanf(infile, '%c', 4);
    while (notdone == 4)
        % Every 4 chars read in is 3 out
        a = uint8(ch); % convert to uint8
        
        % Convert to indices 
        v1 = strfind(base64, a(1)) - 1;
        v2 = strfind(base64, a(2)) - 1;
        v3 = strfind(base64, a(3)) - 1;
        v4 = strfind(base64, a(4)) - 1;
        % Indices are 0..64
        bits1 = [bitget(v1, 1:6), bitget(v2, 1:2)];
        bits2 = [bitget(v2, 3:6), bitget(v3, 1:4)];
        bits3 = [bitget(v3, 5:6), bitget(v4, 1:6)];
        % Convert bits to 0..255
        v1 = uint8(sum(binvals2 .* double(bits1))) ;
        v2 = uint8(sum(binvals2 .* double(bits2))) ;
        % This appends a 0 if the file is encoded then decoded.
        % For files that need an exact decoding, this is a problem.
        v3 = uint8(sum(binvals2 .* double(bits3))) ;
        fprintf(outfile, '%c%c%c', v1, v2, v3);
        % Get more
        [ch, notdone] = fscanf(infile, '%c', 4);
    end
    % Assume we end on an even boundary of 4.
    % This might not be true for other encoders.
    % Close the files
    fclose(infile);
    fclose(outfile);
