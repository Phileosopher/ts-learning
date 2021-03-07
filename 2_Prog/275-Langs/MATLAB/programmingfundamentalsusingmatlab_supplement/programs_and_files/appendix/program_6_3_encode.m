% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_6_3_encode.m

    filename1 = 'somebinaryfile';
    filename2 = 'somebinaryfile.txt';
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
    binvals = [1, 2, 4, 8, 16, 32];
    [ch, notdone] = fscanf(infile, '%c', 3);
    while (notdone == 3)
        % Every 3 chars read in is 4 out
        a = uint8(ch); % convert to uint8
        
        % Isolate bits. 
        bits1 = bitget(a(1), 1:6);
        bits2 = [bitget(a(1), 7:8), bitget(a(2),1:4)];
        bits3 = [bitget(a(2), 5:8), bitget(a(3),1:2)];
        bits4 = bitget(a(3), 3:8);
        % Convert bits to index (0 to 63) + 1
        v1 = sum(binvals .* double(bits1)) + 1;
        v2 = sum(binvals .* double(bits2)) + 1;
        v3 = sum(binvals .* double(bits3)) + 1;
        v4 = sum(binvals .* double(bits4)) + 1;
        % Form a new set of base64 chars
        outchars = [ base64(v1), base64(v2), ...
                     base64(v3), base64(v4)];
        fwrite(outfile, outchars);
        % Get more
        [ch, notdone] = fscanf(infile, '%c', 3);
    end
    % Process the last few chars
    a = uint8(ch);
    a(notdone+1:3) = 0;
    bits1 = bitget(a(1), 1:6);
    bits2 = [bitget(a(1), 7:8), bitget(a(2),1:4)];
    bits3 = [bitget(a(2), 5:8), bitget(a(3),1:2)];
    v1 = sum(binvals .* double(bits1)) + 1;
    v2 = sum(binvals .* double(bits2)) + 1;
    v3 = sum(binvals .* double(bits3)) + 1;
    v4 = 65;
    if (notdone < 2) 
        v3 = 65;
    end
    outchars = [ base64(v1), base64(v2), ...
                 base64(v3), base64(v4)];
    fwrite(outfile, outchars);
    % Close the files
    fclose(infile);
    fclose(outfile);
