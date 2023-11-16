function P = Polynomial_Features(x1,x2,D)
    if D == 0
        n = size(x1,1);
        P = ones(n,1);
    else
        P = [Polynomial_Features(x1,x2,D-1) x1.^(D:-1:0).*x2.^(0:1:D)];
    end
end
