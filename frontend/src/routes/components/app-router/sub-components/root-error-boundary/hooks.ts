import { useRouteError } from "react-router-dom";

export const useRootErrorBoundary = () => {
  const error = useRouteError();
  return { error };
};
