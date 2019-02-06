function [ labelIm, num ] = FindComponentLabels( im, se )
%FINDCOMPONENTLABELS Summary of this function goes here
%   Detailed explanation goes here

% Ben Gibbons Assignment 5

[row, col] = size(im);
Lable = zeros([row col]);
num = 0;

for i = 1:row
    for j = 1:col

        if(im(i,j) == 1)

        num = num+1;
        X = zeros([row col]);
        X(i,j) = 1;

        X0=im&imdilate(X,se);
        
        while(~isequal(X,X0))
            X = X0;
            X0 = im & imdilate(X,se);
        end

    Pos = find(X0==1);

    im(Pos) = 0;

    Lable(Pos) = num;

        end
    end
end
labelIm = Lable;


end

