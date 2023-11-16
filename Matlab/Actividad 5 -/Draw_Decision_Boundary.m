function Draw_Decision_Boundary (x1,x2,w,D)
    bounds = [min(x1) max(x1) min(x2) max(x2)];

    Step = 50;
    [X,Y] = meshgrid(linspace(bounds(1),bounds(2),Step),linspace(bounds(3),bounds(4),Step));
    Z = zeros(Step,Step);
    
    for i=1:Step
        for j=1:Step
            X_Pol = Polynomial_Features(X(i,j),Y(i,j),D);
            Z(i,j) = X_Pol*w;
        end
    end

    contour(X,Y,Z,[0, 0],'LineWidth',2)
end
