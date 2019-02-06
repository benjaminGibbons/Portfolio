%Ben Gibbons Assignment 3

function filteredIm = AverageFiltering(im,mask)

[dim,dim2] = size(mask);
imDim = size(im);
%check mask dimensions
if (dim~=dim2)
    disp('dimensions of mask must be square m=n')
    return 
elseif(mod(dim,2)==0||mod(dim2,2)==0)
    disp('dimensions of mask must be odd n%2!=0')
    return 
end

mask = mask*(1/(sum(mask(:))));


%pad im with zeros where pad = ceiling mask dim/2
padSz = uint64(dim-1);
%get start end locations in newIm
s = uint64(1+(padSz/2));
xe = uint64(imDim(1)+(padSz/2));
ye = uint64(imDim(2)+(padSz/2));
%make padded im
newIm(imDim(1)+padSz,imDim(2)+padSz)= uint8(0);
newIm(s:xe, s:ye)=im(:,:);
%preallocate filteredIm
filteredIm(imDim(1),imDim(2)) = uint8(0);

%apply mask 
for i = 1:imDim(1)
    for j = 1:imDim(2)
        submat = newIm(i:i+dim-1,j:j+dim-1);        
        filteredIm(i,j) = uint8(sum(double(submat(:)).*mask(:)));
    end
end
end




